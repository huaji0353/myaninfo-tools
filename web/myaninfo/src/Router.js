import React,{Component} from 'react'
import {
    BrowserRouter as Router,
    Route,
} from 'react-router-dom'
import App from './App';
import home from  './home'
import Switch from "react-router-dom/es/Switch";
import Head from "./component/Head"
import Side from "./component/Side";
import {MuiThemeProvider} from "material-ui";

class IndexRouter extends Component {
    constructor(props) {
        super(props);
        this.state = {open: false};
    }

    handleToggle = () => this.setState({open: !this.state.open});

    render(){
        return <Router>
                    <MuiThemeProvider>
                        <div>
                        <Route render={()=> <Head onClick={this.handleToggle}/>} />
                        <Route render={()=> <Side handleToggle={this.handleToggle} open={this.state.open}/>}/>
                        <Switch>
                                <Route path="/home" component={home}/>
                                <Route path="/" component={App}/>
                        </Switch>
                        </div>

                    </MuiThemeProvider>
                </Router>
    }
}

export default IndexRouter