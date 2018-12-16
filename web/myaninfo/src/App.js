import React, { Component } from 'react';
import AnimeDesc from './component/AnimeDesc'
import Recommend from './component/Recommend'
import Appraisal from "./component/Appraisal";
import Card from "@material-ui/core/es/Card/Card";
import MuiThemeProvider from "@material-ui/core/es/styles/MuiThemeProvider";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {open: false};
    }





    render() {
    return (

               <Card>
               <AnimeDesc img={"https://huaji0353.coding.me/assets/img/testpic.jpg"} tags={["test","test"]}/>
               <Appraisal/>
               <Recommend/>
               </Card>
    );
  }
}

export default App;
