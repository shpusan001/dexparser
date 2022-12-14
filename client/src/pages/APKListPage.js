import Header from "../component/common/Header";
import ApkList from "../component/apk_list/ApkList";
import ApkUploadForm from "../component/apk_list/ApkUploadForm";
import ApkRemoveForm from "../component/apk_list/ApkRemoveForm";
import { useEffect, useState } from "react";

export default function ApkListPage() {
  return (
    <>
      <Header />
      <div class="container mt-3">
        <h1>ApkList</h1>
        <hr />
        <div class="ms-3">
          <ApkUploadForm />
          <hr />
          <ApkRemoveForm />
          <hr />
          <ApkList />
        </div>
      </div>
    </>
  );
}
