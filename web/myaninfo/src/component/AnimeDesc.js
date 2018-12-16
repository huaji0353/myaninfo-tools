import React, { Component } from 'react';
import { CardText } from 'material-ui';
import Grid from '@material-ui/core/Grid';
import Button from "@material-ui/core/es/Button/Button";
import Card from '@material-ui/core/Card';
import CardContent from "@material-ui/core/es/CardContent/CardContent";
import PropTypes from 'prop-types';

class AnimeDesc extends Component {
    constructor(props) {
        super(props);
    }
    Style  = {
        img:{
            height:"100%",
            width:"100%"
        },
        button: {
            margin: "10px",
        },
    };

    render() {
        return (
            <Card>
                <CardContent>
            <Grid container spacing={0} >
                <Grid item xs={3}>
                <img src={this.props.img} style={this.Style.img}/>
                </Grid>
                <Grid item xs={9}>
                    <CardText>
                <h2>{this.props.title}</h2>
                        <h2>{this.props.author}</h2>
                    </CardText>

                    <Grid item xs={12} style={this.Style.button}>
                        {
                            this.props.tags.map(name => (
                                <Button  variant="contained" color="primary" style={this.Style.button}>
                                    {name}
                                </Button>
                                )
                            )
                        }

                        </Grid>


                <CardText>
                    {this.props.desc}
                </CardText>
                </Grid>
            </Grid>
                </CardContent>
            </Card>


        )
    }
}
const propTypes = {
    title:PropTypes.string,
    author:PropTypes.string,
    desc:PropTypes.string,
    tags:PropTypes.array,
    img:PropTypes.string,
};

AnimeDesc.propTypes = propTypes;

const noData = "暂无数据";
const defaultProps = {
    title:noData,
    author:noData,
    desc:noData,
    tags:[],
};

AnimeDesc.defaultProps = defaultProps;

export default AnimeDesc;
