import { Routes, Route } from "react-router-dom";
import { GoodsHub} from "../pages/GoodsHub/GoodsHub";
import { Catalog } from "../pages/Catalog/Catalog";
import { ProductDetails } from "../pages/Catalog/ProductDetails";
import { LoginPage } from "../pages/LoginPage/LoginPage";
// import { RegisterPage } from "../pages/RegisterPage/RegisterPage"
import { Messages } from "../pages/Messages/Messages";
import { Favorites } from "../pages/Favorites/Favorites";
import { Basket } from "../pages/Basket/Basket";
import { NotFoundPage } from "../pages/NotFoundPage/NotFoundPage";
import { SharedLayout } from "./SharedLayout";

export const App = () => {
  return (
      <Routes>
        <Route path="/" element={<SharedLayout />} >
          <Route index element={<GoodsHub />} />
          <Route path="/catalog" element={<Catalog />} />
          <Route path="/catalog/:id" element={<ProductDetails />} />
          {/* <Route path="/register" element={<RegisterPage />} /> */}
          <Route path="/login" element={<LoginPage />} />
          <Route path="/messages" element={<Messages />} />
          <Route path="/favorites" element={<Favorites />} />
          <Route path="/basket" element={<Basket />} />
          <Route path="*" element={<NotFoundPage />} /> 
        </Route>
      </Routes>
    
  );
};



// import { Routes, Route } from "react-router-dom";
// import { Container, Header, Logo, Link } from "./App.styled";

// import { GoodsHub} from "../pages/GoodsHub/GoodsHub";
// import { Catalog } from "../pages/Catalog/Catalog";
// import { ProductDetails } from "../pages/Catalog/ProductDetails";
// import { LoginPage } from "../pages/LoginPage/LoginPage";
// // import { RegisterPage } from "../pages/RegisterPage/RegisterPage"
// import { Messages } from "../pages/Messages/Messages";
// import { Favorites } from "../pages/Favorites/Favorites";
// import { Basket } from "../pages/Basket/Basket";
// import { NotFoundPage } from "../pages/NotFoundPage/NotFoundPage";

// export const App = () => {
//   return (
//     <Container>
      
//        <Header>
//         <Logo>
//           <span role="img" aria-label="computer icon">
//             💻
//           </span>{" "}
//           <Link to="/" end>GoodsHub</Link>
//         </Logo>
//         <Link to="/catalog">Catalog</Link>
//         <nav>
//           <Link to="/login">Login</Link>
//           <Link to="/messages">Messages</Link>
//           <Link to="/favorites">Favorites</Link>
//           <Link to="/basket">Basket</Link>
//         </nav>
//       </Header>

//       <Routes>
//         <Route path="/" element={<GoodsHub />} />
//         <Route path="/catalog" element={<Catalog />} />
//         <Route path="/catalog/:id" element={<ProductDetails />} />
//         {/* <Route path="/register" element={<RegisterPage />} /> */}
//         <Route path="/login" element={<LoginPage />} />
//         <Route path="/messages" element={<Messages />} />
//         <Route path="/favorites" element={<Favorites />} />
//         <Route path="/basket" element={<Basket />} />
//         <Route path="*" element={<NotFoundPage/>} /> 
//       </Routes>
//     </Container>
//   );
// };