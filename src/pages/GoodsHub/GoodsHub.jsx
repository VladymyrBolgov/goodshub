import React from "react";
import { getProducts } from "../../fakeHomeAPI";
import { ProductList } from "../../components/ProductList/ProductList";

export const GoodsHub = () => {
    const products = getProducts();
    return (
        <main>
                    <br></br>
            <img src="https://via.placeholder.com/960x240" alt="" />
                    <br></br>
            <main>
                <h2>Promotional offers</h2>
                    <br></br>
                <ProductList products={products} />
                    <br></br>
                <h2>Hot new products</h2>
                    <br></br>
                <ProductList products={products} />
                    <br></br>
                <h2>More products to choose from</h2>
                    <br></br>
                <ProductList products={products} />
            </main>
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
             
        </main>
    )
}
