import { ProductList } from "../../components/ProductList/ProductList";
import { getProducts } from "../../fakeAPI";

export const Catalog = () => {
  const products = getProducts();
  return (
    <main>
      <ProductList products={products} />
    </main>
  );
};