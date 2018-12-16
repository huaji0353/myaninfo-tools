import React, { Component } from 'react';
import Card from '@material-ui/core/Card';
import CardContent from "@material-ui/core/es/CardContent/CardContent";
import Typography from "@material-ui/core/es/Typography/Typography";
import GridList from "@material-ui/core/es/GridList/GridList";
import GridListTile from "@material-ui/core/es/GridListTile/GridListTile";
import GridListTileBar from "@material-ui/core/es/GridListTileBar/GridListTileBar";
import PropTypes from 'prop-types';

class Recommend extends Component{
    constructor(props) {
        super(props);
    }



    styles = {
        card: {
            minWidth: 275,
        },
        bullet: {
            display: 'inline-block',
            margin: '0 2px',
            transform: 'scale(0.8)',
        },
        title: {
            marginBottom: 16,
            fontSize: 14,
        },
        pos: {
            marginBottom: 12,
        },
        img: {
          //   width:"50%",
        }
    };


    render(){
        return <Card style={this.styles.pos}>
            <CardContent>
                <Typography  variant="headline" component="h3">
                    番剧推荐
                </Typography>
                <GridList cellHeight={this.props.cellHeight} cols={this.props.cols}>
                        {this.props.data.map(tile => (
                            <GridListTile key={tile.img}>
                                <img src={tile.img}  alt={tile.title} style={this.styles.img}/>
                                <GridListTileBar
                                    title={tile.title}
                                />
                            </GridListTile>
                        ))}
                </GridList>
                 </CardContent>
                </Card>
    }
}

const titleData = [
    {
        img: "https://huaji0353.coding.me/assets/img/testpic.jpg",
        title:"神乐家族"
    },
    {
        img: "https://huaji0353.coding.me/assets/img/testpic.jpg",
        title:"神乐家族"
    }
]

const propTypes = {
    data:PropTypes.array,
    cols:PropTypes.number,
    cellHeight:PropTypes.number,
};

const  defaultProps = {
    data:titleData,
    cols:4,
    cellHeight:180,
};

Recommend.propTypes = propTypes;
Recommend.defaultProps = defaultProps

export default Recommend