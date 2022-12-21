import { createAction, handleActions } from "redux-actions";

const SET_HOST = "setting_SET_HOST";

export const setMainHost = createAction(SET_HOST, (data) => data);

const initialState = {
  host: "http://localhost:8000",
};

const setting = handleActions(
  {
    [SET_HOST]: (state, { payload: data }) => ({
      ...state,
      host: data,
    }),
  },
  initialState
);

export default setting;
