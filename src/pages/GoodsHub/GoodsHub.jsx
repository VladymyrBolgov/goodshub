import React from "react";
import { getProducts } from "../../fakeHomeAPI";
import { ProductList } from "../../components/ProductList/ProductList";
import { Container } from "./GoodsHab.styled";
import {StyledTitle, BoxImg} from "./GoodsHab.styled"

export const GoodsHub = () => {
    const products = getProducts();
    return (
        <main>
             <Container>
                
                <BoxImg>
                    <img src="https://via.placeholder.com/1176x400" alt="" />
                </BoxImg>
                  
            
                <StyledTitle>Promotional offers</StyledTitle>
                    
                <ProductList products={products} />
                    
                <StyledTitle>Hot new products</StyledTitle>
                    
                <ProductList products={products} />
                   
                <StyledTitle>More products to choose from</StyledTitle>
                   
                <ProductList products={products} />
            
            <br></br>
            <br></br>
            <br></br>
            
            <footer>
                <h2>Logo GoodsHub</h2>
                <br></br>
                <p>Privacy Policy</p>
                <p>Help&FAQ</p>
                <p>Payment and delivery</p>
                <p>Return Policy</p>
                <p>How to sell and buy?</p>
                <br></br>
                <p>© 2023 GoodsHub. All rights reserved.</p>
            </footer>
         </Container>    
        </main>
    )
}
