/** @odoo-module */
import { loadJS } from "@web/core/assets"
const { Component, onWillStart, useRef, onMounted } = owl


export class ChartRenderer extends Component {
    setup(){
        this.chartRef = useRef("chart")
        onWillStart(async ()=>{
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js")
        })

        onMounted(()=>this.renderChart())
    }

    async renderChart(){
        new Chart(this.chartRef.el,
        {
          type: this.props.type,
          data: await this.props.config.data,
          options: {
            // onclick:(e)=>{

            // }
            responsive: true,
            plugins: {
              legend: {
                position: 'bottom',
              },
              title: {
                display: true,
                text: this.props.title,
                position: 'bottom',
              }
            },
            scales:'scales' in this.props.config ? this.props.config.scales : {},
          },
        }
      );
    }
}

ChartRenderer.template = "owl_dashboard.ChartRenderer"