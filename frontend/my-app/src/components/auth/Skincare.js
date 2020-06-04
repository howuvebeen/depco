import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { getproductList } from "../../actions/authActions";
import { Link } from "react-router-dom";

class Skincare extends Component {

    static propTypes = {
        getproductList: PropTypes.func.isRequired,
        product: PropTypes.object
    };

    componentWillMount() {
        this.props.getproductList();
    }

    renderProductList() {
        const products  = this.props.product;
        
        function Star(star){
            if (star < 1){
              return "☆☆☆☆☆";
            } else if (star >=1 && star <2){
              return "★☆☆☆☆"
            } else if (star >=2 && star <3){
              return "★★☆☆☆"
            } else if (star >=3 && star <4){
              return "★★★☆☆"
            } else if (star >=4 && star <5){
              return "★★★★☆"
            } else {
              return "★★★★★"
            }
          }

        if (products) {
            return (
                <div class="row p-3">
                    {products.map(product => (
                        <div class="p-5">
                            <div>
                                <p>{product.company}</p>                               
                                <Link to={`/skincare/${product.pk}`}><h4>{product.name}</h4></Link>
                            </div>
                            <div>
                                {Star(product.average_star)}
                            </div>
                        </div>
                    ))}
                </div>
            );
        }
        return null;
    }

    render() {
        return (
            <div class="d-flex flex-column align-items-center p-3">
                {this.renderProductList()}
            </div>
        );
    }
}

function mapStateToProps(state) {
    return {
        product: state.auth.product
    }

}

export default connect(mapStateToProps, { getproductList } )( Skincare );