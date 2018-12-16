import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Drawer from "@material-ui/core/es/Drawer/Drawer";
import MenuItem from "@material-ui/core/es/MenuItem/MenuItem";

class side extends Component {

    render() {
    return <Drawer
            docked={false}
            width={200}
            open={this.props.open}
            onRequestChange={(open) => this.props.handleToggle({open})}
            >
                <h2>myaninfo</h2>
                {this.props.menu}
                <MenuItem onClick={this.handleClose}>番剧列表</MenuItem>
            </Drawer>
    }
}

const propTypes = {
    open:PropTypes.bool,
    handleToggle:PropTypes.func,
    menu:PropTypes.node,
};
const defaultProps = {
    open:false,
    handleToggle:()=>{},
};
side.propTypes = propTypes;
side.defaultProps = defaultProps;

export default side