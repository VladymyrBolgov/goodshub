import styled from "styled-components";

export const Container = styled.div`
  padding: 0 130px;
  display: grid;
  grid-template-columns: repeat(auto-fit, 175px);
  gap: 24px;
`;

export const CardWrapper = styled.div`
  border: 1px solid black;
  border-radius: 4px;

  > a {
    text-decoration: none;
  }
`;

export const ProductName = styled.h3`
  padding: 4px;
  margin-top: 8px;
  margin-bottom: 0;
  color: black;
`;
