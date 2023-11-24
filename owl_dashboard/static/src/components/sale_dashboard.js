/**@odoo-module */
import { registry } from "@web/core/registry";
import { KpiCard } from "./kpi_card/kpi_card";
import { ChartRenderer } from "./chart_renderer/chart_renderer";
import { useService } from "@web/core/utils/hooks";
const { Component, onWillStart, useRef, onMounted, useState } = owl;
const { DateTime } = luxon;
import { getColor } from "@web/core/colors/colors";
export class OwlSalesDashboard extends Component {
  async getTopProducts() {
    let domain = [["state", "in", ["sale"]]];
    if (this.state.period > 0) {
      domain.push(["date", ">", this.state.current_date]);
    }
    const top_product_data = await this.orm.readGroup(
      "sale.report",
      domain,
      ["product_id", "price_total"],
      ["product_id"],
      {limit:4,orderby:"price_total desc"}
    );
  
    this.state.topProduct = {
      data: {
        labels: top_product_data.map((d) => d.product_id[1]),
        datasets: [
          {
            label: "Total",
            data: top_product_data.map((d) => d.price_total),
            hoverOffset: 4,
            backgroundColor: top_product_data.map((_, index) =>
              getColor(index)
            ),
          },
          {
            label: "Count",
            data: top_product_data.map((d) => d.product_id_count),
            hoverOffset: 4,
            backgroundColor: top_product_data.map((_, index) =>
              getColor(index)
            ),
          },
        ],
      },
      domain,
      label_field:'product_id'
    };
  }
  async getTopSalesPeople() {

    let domain = [["state", "in", ["sale"]]];
    if (this.state.period > 0) {
      domain.push(["date", ">", this.state.current_date]);
    }
    const top_sale_person = await this.orm.readGroup(
      "sale.report",
      domain,
      ["user_id", "price_total"],
      ["user_id"],
      {limit:4,orderby:"price_total desc"}
    );
  
    this.state.toSalesPeople = {
      data: {
        labels: top_sale_person.map((d) => d.user_id[1]),
        datasets: [
          {
            label: "Total",
            data: top_sale_person.map((d) => d.price_total),
            hoverOffset: 4,
            backgroundColor: top_sale_person.map((_, index) =>
              getColor(index)
            ),
          },
         
        ],
      },
      domain,
      label_field:'user_id'
    };
   
  }
  async getMonthlySales() {
    
    let domain = [["state", "in", ["draft","sent","sale"]]];
    if (this.state.period > 0) {
      domain.push(["date", ">", this.state.current_date]);
    }
    const MonthlySales = await this.orm.readGroup(
      "sale.report",
      domain,
      ["date","state", "price_total"],
      ["date","state"],
      {orderby:"date",lazy:false}
    );

    // const labels = [... new Set (data.map(d => d.date))]
    // const quotations = data.filter(d => d.state == 'draft' || d.state == 'sent')
    // const orders = data.filter(d => ['sale', 'done'].includes(d.state))

    this.state.monthlySales = {
      data: {
        labels: [... new Set(MonthlySales.map((d) => d.date))
        ],
        datasets: [
          {
            label: "Quotation",
            data: MonthlySales.filter(d=>d.state == 'draft' || d.state == 'sent').map((d) => d.price_total),
            hoverOffset: 4,
            backgroundColor:"red"
            
          },
          
          {
            label: "Orders",
            data: MonthlySales.filter(d=>['sale'].includes(d.state)).map((d) => d.price_total),
            hoverOffset: 4,
            backgroundColor: "green"
          },
         
        ],
      },
      domain,
      label_field:'date'
    };
  }
  async getPartnerOrders() {
    let domain = [["state", "in", ["draft","sent","sale"]]];
    if (this.state.period > 0) {
      domain.push(["date", ">", this.state.current_date]);
    }
    const partner_id_data = await this.orm.readGroup(
      "sale.report",
      domain,
      ["partner_id", "price_total","product_uom_qty"],
      ["partner_id"],
      {orderby:"partner_id",lazy:false}
    );
    // console.log(partner_id_data);

    this.state.partnerOrders = {
      data: {
        labels: partner_id_data.map(d => d.partner_id[1]),
        datasets: [
          {
            label: "Total Amount",
            data: partner_id_data.map(d => d.price_total),
            hoverOffset: 4,
            backgroundColor:"orange",
            yAxisID:"Total",
            order:1
            
          },
          
          {
            label: "Ordered QTY",
            data: partner_id_data.map(d => d.product_uom_qty),
            hoverOffset: 4,
            type:"line",
            backgroundColor: "blue",
            borderColor:"blue",
            yAxisID:"Qty",
            order:0

          },
          
         
        ],
      },
      scales:
          {
         
            Qty:{
              position:"right"
            }
          },
          domain,
          label_field:'partner_id'
    };
  }

  setup() {
    this.state = useState({
      quotation: {
        value: 10,
        percentage: 10,
      },
      period: 90,
    });
    this.orm = useService("orm");
    this.action = useService("action");
    onWillStart(async () => {
      this.getDates();
      await this.getQuotation();
      await this.getOrders();
      await this.getPartnerOrders();
      await this.getMonthlySales();
      await this.getTopProducts();
      await this.getTopSalesPeople();
    });

    // })
  }
  async onChangePeriod() {
    this.getDates();
    await this.getQuotation();
    await this.getOrders();
  }
  async getQuotation() {
    let domain = [["state", "in", ["sent", "draft"]]];
    if (this.state.period > 0) {
      domain.push(["date_order", ">", this.state.current_date]);
    }
    const data = await this.orm.searchCount("sale.order", domain);
    let prev_domain = [["state", "in", ["sent", "draft"]]];
    if (this.state.period > 0) {
      prev_domain.push(
        ["date_order", ">", this.state.prev_date],
        ["date_order", "<=", this.state.current_date]
      );
    }
    const prev_data = await this.orm.searchCount("sale.order", prev_domain);
    const percentage = ((data - prev_data) / prev_data) * 100;
    this.state.quotation.value = data;
    this.state.quotation.percentage = percentage.toFixed(2);
    // console.log(`${percentage} ${prev_data}`);
  }

  async getOrders() {
    let domain = [["state", "in", ["sale"]]];
    if (this.state.period > 0) {
      domain.push(["date_order", ">", this.state.current_date]);
    }
    const data = await this.orm.searchCount("sale.order", domain);
    let prev_domain = [["state", "in", ["sale"]]];
    if (this.state.period > 0) {
      prev_domain.push(
        ["date_order", ">", this.state.prev_date],
        ["date_order", "<=", this.state.current_date]
      );
    }
    const prev_data = await this.orm.searchCount("sale.order", prev_domain);

    const percentage = ((data - prev_data) / prev_data) * 100;

    const current_revenue = await this.orm.readGroup(
      "sale.order",
      domain,
      ["amount_total:sum"],
      []
    );

    const prev_revenue = await this.orm.readGroup(
      "sale.order",
      prev_domain,
      ["amount_total:sum"],
      []
    );
    const revenue_percentage =
      ((current_revenue[0].amount_total - prev_revenue[0].amount_total) /
        prev_revenue[0].amount_total) *
      100;

    //average order value
    const current_average = await this.orm.readGroup(
      "sale.order",
      domain,
      ["amount_total:avg"],
      []
    );

    const prev_average = await this.orm.readGroup(
      "sale.order",
      prev_domain,
      ["amount_total:avg"],
      []
    );

    const average_percentage =
      ((current_average[0].amount_total - prev_average[0].amount_total) /
        prev_average[0].amount_total) *
      100;

    this.state.orders = {
      value: data,
      percentage: percentage.toFixed(2),
      revenue: `${(current_revenue[0].amount_total / 1000).toFixed(2)}K Rs`,
      average: `${(current_average[0].amount_total / 1000).toFixed(2)}K Rs`,
      revenue_percentage: revenue_percentage.toFixed(2),
      average_percentage: average_percentage.toFixed(2),
    };

    // this.state.quotation.value = data;
    // this.state.quotation.percentage = percentage.toFixed(2);
    // console.log(`${percentage} ${data}`);
  }

  getDates() {
    this.state.current_date = DateTime.now()
      .minus({ days: this.state.period })
      .toFormat("MM/dd/yyyy");
    this.state.prev_date = DateTime.now()
      .minus({ days: this.state.period * 2 })
      .toFormat("MM/dd/yyyy");
    console.log(this.state.current_date, this.state.prev_date);
  }

  async viewQuotation() {
    let domain = [["state", "in", ["sent", "draft"]]];
    if (this.state.period > 0) {
      domain.push(["date_order", ">", this.state.current_date]);
    }
    let action_id = await this.orm.searchRead(
      "ir.model.data",
      [["name", "=", "view_quotation_tree_with_onboarding"]],
      ["res_id"]
    );
    this.action.doAction({
      type: "ir.actions.act_window",
      name: "Quotations",
      res_model: "sale.order",
      domain,
      views: [
        [action_id.length > 0 ? action_id[0].res_id : false, "list"],
        [false, "form"],
      ],
    });
  }

  viewOrders() {
    let domain = [["state", "in", ["sale"]]];
    if (this.state.period > 0) {
      domain.push(["date_order", ">", this.state.current_date]);
    }
    this.action.doAction({
      type: "ir.actions.act_window",
      name: "Orders",
      res_model: "sale.order",
      domain,
      context: { group_by: "date_order" },
      views: [
        [false, "list"],
        [false, "form"],
      ],
    });
  }

  viewRevenue() {
    let domain = [["state", "in", ["sale"]]];
    if (this.state.period > 0) {
      domain.push(["date_order", ">", this.state.current_date]);
    }
    this.action.doAction({
      type: "ir.actions.act_window",
      name: "Orders",
      res_model: "sale.order",
      domain,
      context: { group_by: "date_order" },
      views: [
        [false, "pivot"],
        [false, "form"],
      ],
    });
  }
  // viewQuotation() {
  //   this.action.doAction("sale.action_orders");
  // }
}

OwlSalesDashboard.template = "owl_dashboard.OwlSalesDashboard";
OwlSalesDashboard.components = { KpiCard, ChartRenderer };
registry
  .category("actions")
  .add("owl_dashboard.sale_dashboard", OwlSalesDashboard);
