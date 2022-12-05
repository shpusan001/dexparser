export default function ApkUploadForm() {
  return (
    <>
      <form class="row row-cols-lg-auto g-3 align-items-center my-3">
        <div class="col-12">
          <div class="input-group">
            <input
              type="file"
              accept=".apk"
              class="form-control"
              placeholder="Username"
            />
          </div>
        </div>
        <div class="col-12">
          <button type="submit" class="btn btn-primary">
            Upload
          </button>
        </div>
      </form>
    </>
  );
}
