export const SET_CART = "SET_CART"; // 액션 타입 (Action Type) 정의

export const setCart = (newCart) => {
  return {
    type: SET_CART,
    payload: newCart,
  };
};
