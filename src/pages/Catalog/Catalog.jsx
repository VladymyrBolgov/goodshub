// export const Catalog = () => {
//     return (
//       <main>
//         <h1>Catalog</h1>
//         <br></br>
//         <p>это каталог товара, кнопка есть у всех пользователей</p>
//         <br></br>
//         <ol>Стиральные машины
//           <li>Лж</li>
//           <li>Самсунг</li>
//           <li>Индезит</li>
//           <li>Аристон</li>
//         </ol>
//         <br></br>
//         <ol>Стиральные машины
//           <li>Лж</li>
//           <li>Самсунг</li>
//           <li>Индезит</li>
//           <li>Аристон</li>
//         </ol>
//       </main>
//     );
// };
  
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