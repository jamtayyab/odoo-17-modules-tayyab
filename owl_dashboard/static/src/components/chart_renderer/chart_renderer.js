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
            // console.log(active);
            const label = e.chart.data.labels[active[0].index];
            let new_domain = domain || [];
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
                // console.log(month_start,month_end);
                new_domain.push(
                  ["date", ">=", month_start],
                  ["date", "<=", month_end]
                );
              } else {
                new_domain.push([label_field, "=", label]);
              }
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
