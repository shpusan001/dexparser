import axios from "axios";

const client = axios.create();

axios.defaults.withCredentials = true;

client.defaults.headers.common["Authorization"] = "temp_key";
client.defaults.baseURL = "default";

//인서셉터 설정
axios.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default client;
