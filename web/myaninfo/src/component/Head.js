import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {AppBar, IconButton, Toolbar, Typography} from "@material-ui/core/es/index";
import MenuIcon from '@material-ui/icons/Menu';



class head extends Component {

    style = {
        menuButton: {
            marginLeft: -12,
            marginRight: 20,
        },
    };

    render() {
        return  <AppBar
                    iconClassNameRight="muidocs-icon-navigation-expand-more"
                    onLeftIconButtonClick={this.props.onClick}
                 >
                    <Toolbar>
                        <IconButton className={this.style.menuButton} color="inherit" aria-label="Menu">
                            <MenuIcon />
                        </IconButton>
                        <Typography variant="title" color="inherit">
                            myaninfo
                        </Typography>
                    </Toolbar>
                 </AppBar>
    }
}

const propTypes = {
    onClick:PropTypes.func,
};
const defaultProps = {
    onClick:()=>{}
};
head.propTypes = propTypes;
head.defaultProps = defaultProps;

export default head