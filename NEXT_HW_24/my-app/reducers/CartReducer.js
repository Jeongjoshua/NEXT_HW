import { SET_CART } from "../actions/CartActions";

const initialState = {
  cart: [],
};

export const cartReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_CART:
      return {
        ...state,
        cart: action.payload, // 액션에 담긴 새로운 cart 값으로 상태 업데이트
      };
    default:
      return state;
  }
};
