/**@odoo-module */
import { registry } from "@web/core/registry";
import { KpiCard } from "./kpi_card/kpi_card";
import { ChartRenderer } from "./chart_renderer/chart_renderer";
import { useService } from "@web/core/utils/hooks";
const { Component, onWillStart, useRef, onMounted, useState } = owl;
const { DateTime } = luxon;
export class OwlSalesDashboard extends Component {
  setup() {
    // this.ref =useRef("chart")
    // onWillStart(async ()=>{
    //     await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js")
    // })
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

  viewQuotation(){
  this.action.doAction("sale.action_quotations_with_onboarding")

  }
}


OwlSalesDashboard.template = "owl_dashboard.OwlSalesDashboard";
OwlSalesDashboard.components = { KpiCard, ChartRenderer };
registry
  .category("actions")
  .add("owl_dashboard.sale_dashboard", OwlSalesDashboard);
