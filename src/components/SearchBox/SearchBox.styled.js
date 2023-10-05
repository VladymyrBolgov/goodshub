import styled from "styled-components";
import { HiSearch } from "react-icons/hi";

export const Wrapper = styled.div`
  display: inline-flex;
  align-items: center;
  position: relative;
  text-transform: uppercase;
`;

export const Input = styled.input`
  padding-left: 30px;
  border-radius: 4px 0 0 4px;
  width: 476px;
  height: 44px;
  font: inherit;
`;

export const Button = styled.button`
 border-radius: 0 4px 4px 0 ;
 width: 76px;
 height: 49px;
 background-color: #1A43E7;
 cursor: pointer;
`;

export const Icon = styled(HiSearch)`
  width: 20px;
  height: 20px;
  position: absolute;
  left: 7px;
`;

