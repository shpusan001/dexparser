import client from "./client";

export const getSync = (data) =>
  client.get("/sync", { params: data }, { withCredentials: true });
