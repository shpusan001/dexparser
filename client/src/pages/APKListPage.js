import Header from "../module/Header";
import ApkList from "../module/ApkList";
import ApkUploadForm from "../module/ApkUploadForm";
import ApkRemoveForm from "../module/ApkRemoveForm";

export default function ApkListPage() {
  return (
    <>
      <Header />
      <div class="container">
        <ApkUploadForm />
        <ApkRemoveForm />
        <ApkList />
      </div>
    </>
  );
}
