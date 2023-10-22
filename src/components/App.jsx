import { Routes, Route } from "react-router-dom";
import { GoodsHub } from "../pages/GoodsHub/GoodsHub";
import { Catalog  } from "../pages/Catalog/Catalog";
import { Catalogs } from "../pages/Catalogs/Catalogs";
import { ProductDetails } from "../pages/Catalogs/ProductDetails";
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
          <Route path="/GoodsHub" element={<GoodsHub />} /> 
              <Route path="/catalog" element={<Catalog />} >
                <Route path="/catalogs" element={<Catalogs />} />
                <Route path="/catalog/:id" element={<ProductDetails />} />
              </Route>
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


