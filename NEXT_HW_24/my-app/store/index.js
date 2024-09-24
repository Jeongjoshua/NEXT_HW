import { configureStore } from "@reduxjs/toolkit";
import { persistStore, persistReducer } from "redux-persist";
import storage from "redux-persist/lib/storage"; // 로컬 스토리지 사용
import { cartReducer } from "../reducers/CartReducer";

// persist 설정
const persistConfig = {
  key: "root",
  storage,
};

// persistedReducer 생성
const persistedReducer = persistReducer(persistConfig, cartReducer);

// configureStore로 store 생성
const store = configureStore({
  reducer: persistedReducer, // persistedReducer를 사용
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false, // redux-persist와 함께 사용할 때 직렬화 검사를 끄는 옵션
    }),
});

// persistor 생성
const persistor = persistStore(store);

export { store, persistor };
