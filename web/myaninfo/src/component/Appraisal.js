import React, { Component } from 'react';
import Card from "@material-ui/core/es/Card/Card";
import {CardText, CardTitle} from "material-ui";
import PropTypes from 'prop-types';


class Appraisal extends Component {
    constructor(props){
        super(props)
    }

    styles = {
        right:{
            marginLeft:"2%"
        }
    };

    render(){
    return <Card >
        <CardTitle>
            <h3>
            番剧评价
            </h3>
        </CardTitle>
            <CardText style={this.styles.right}>
                {this.props.text}
            </CardText>
        </Card>
    }
}

const defaultProps = {
    text: '暂无'
};

const propTypes = {
    // TODO 可能需要使用更强大的类型
    text:PropTypes.string
};

Appraisal.defaultProps = defaultProps;

Appraisal.propTypes = propTypes;



export default Appraisal