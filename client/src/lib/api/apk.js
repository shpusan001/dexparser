import client from "./client";

export const getAPIList = () => client.get("/apk ", { withCredentials: true });

export const uploadApkFile = (data) =>
  client.post("/apk ", data, { withCredentials: true });

export const deleteApkFile = (fileId) =>
  client.delete("/apk ", { fileId: fileId }, { withCredentials: true });
