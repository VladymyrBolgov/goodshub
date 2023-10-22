import { ProductList } from "../../components/ProductList/ProductList";
import { getProducts } from "../../fakeAPI";

export const Catalogs = () => {
  const products = getProducts();
  return (
    <main>
      <ProductList products={products} />
    </main>
  );
};