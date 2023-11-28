/**@odoo-module */
import { registry } from "@web/core/registry";
const { Component,useState } = owl;

export class TodoList extends Component{
setup(){
    this.state =useState({
        taskList:[
            {id:1, name:"todo 1",color:"#FF0000" ,done:false},
            {id:2, name:"todo 2",color:"#FFFFFF", done:true},
        ]
    })
}

}
TodoList.template = "owl_dashboard.todo_list_template"
registry
  .category("actions")
  .add("owl_dashboard.owl_action_todo_list", TodoList);