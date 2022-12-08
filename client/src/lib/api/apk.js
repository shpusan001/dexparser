import client from "./client";

export const getAPIList = (data) =>
  client.get("/apk", { withCredentials: true });

export const uploadApkFile = (data) => {
  client.post("/apk", data, { withCredentials: true });
};

export const deleteApkFile = (data) => {
  client.delete("/apk", { params: data }, { withCredentials: true });
};
