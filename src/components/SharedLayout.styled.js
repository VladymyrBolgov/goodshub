import styled from "styled-components";
import { NavLink } from "react-router-dom";


export const Container = styled.div`
 width: 1440px;
  margin: 0 auto;
  padding: 0 16px;
`;

// export const Container = styled.div`
//   margin: 0 auto;
//   padding: 0 20px;
//   @media screen and (min-width: 320px) {
//     width: 320px;
//   }
//   @media screen and (min-width: 768px) {
//     padding: 0 32px;
//     width: 768px;
//   }
//   @media screen and (min-width: 1280px) {
//     padding: 0 16px;
//     width: 1440px;
//   }
// `;

export const Header = styled.header`
  display: flex;
  align-items: center;
  justify-content: space-between;
  /* width: 1170px; */
  height: 80px;
  gap: 12px;
  margin-bottom: 16px;
  padding: 0 130px;
  background-color: #CCD5FA;
  
  > nav {
    display: flex;
  }
`;

export const Logo = styled.p`
  font-weight: 700;
  margin: 0;
  /* padding: 8px 16px; */
`;


export const Link = styled(NavLink)`
  padding: 8px 16px;
  border-radius: 4px;
  text-decoration: none;
  color: #F76800;
  font-weight: 700;

  &.active {
    color: black;
    /* background-color: orangered; */
  }
`;

