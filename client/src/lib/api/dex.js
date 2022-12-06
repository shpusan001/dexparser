import client from "./client";

export const getParsing = (data) =>
  client.get("/parsing ", { fileId: data }, { withCredentials: true });

export const getSmali = (data) =>
  client.post("/conv/hex2smali ", data, { withCredentials: true });
