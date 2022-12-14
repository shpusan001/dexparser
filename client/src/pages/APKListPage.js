import Header from "../component/Header";
import ApkList from "../component/ApkList";
import ApkUploadForm from "../component/ApkUploadForm";
import ApkRemoveForm from "../component/ApkRemoveForm";
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
