/** @odoo-module */
import { loadJS } from "@web/core/assets";
const { Component, onWillStart, useRef, onMounted } = owl;
import { useService } from "@web/core/utils/hooks";
const { DateTime } = luxon;


export class ChartRenderer extends Component {
  setup() {
    this.chartRef = useRef("chart");
    this.actionService = useService("action");
    onWillStart(async () => {
      await loadJS(
        "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"
      );
    });

    onMounted(() => this.renderChart());
  }

  async renderChart() {
    const chartData = await this.props.config.data;

    new Chart(this.chartRef.el, {
      type: this.props.type,
      data: chartData,
      options: {
        onClick: (e) => {
          const active = e.chart.getActiveElements();   
          const { domain, label_field } = this.props.config;
          if (active.length > 0) {
            const label = e.chart.data.labels[active[0].index];
            const dataset = e.chart.data.datasets[active[0].datasetIndex].label;
            let new_domain = domain ? domain : [];
            console.log(domain)
            console.log(new_domain)
            if (label_field) {
              if (label_field.includes("date")) {
                const [month, year] = label.split(' ');
                const dt = DateTime.fromFormat(month, 'LLLL');
                // console.log(dt);
                const monthNumber = dt.month;  // Get the month number
                const startOfMonth = DateTime.fromObject({ year, month: monthNumber }).startOf('month');
                const month_start = startOfMonth.toFormat('MM/dd/yyyy');
                // console.log(startOfMonth,month_start);
                const endOfMonth = DateTime.fromObject({ year, month: monthNumber }).endOf('month');
                const month_end = endOfMonth.toFormat('MM/dd/yyyy');
                console.log(month_start,month_end);
                new_domain.push(
                  ["date", ">=", month_start],
                  ["date", "<=", month_end]
                );
                // console.log(new_domain);
              } else {
                new_domain.push([label_field, "=", label]);
              }
            }
            if (dataset == 'Quotations'){

              new_domain.push(['state','in',['draft','sent']])
            }
            if (dataset == 'Orders'){

              new_domain.push(['state','in',['sale']])
            }
            this.actionService.doAction({
              type: "ir.actions.act_window",
              name: this.props.title,
              res_model: "sale.report",
              domain: new_domain,
              views: [
                [false, "list"],
                [false, "form"],
              ],
            });
          }
        },
        responsive: true,
        plugins: {
          legend: {
            position: "bottom",
          },
          title: {
            display: true,
            text: this.props.title,
            position: "bottom",
          },
        },
        scales: "scales" in this.props.config ? this.props.config.scales : {},
      },
    });
  }
}

ChartRenderer.template = "owl_dashboard.ChartRenderer";
