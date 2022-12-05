export default function ApkRemoveForm() {
  return (
    <>
      <form class="row row-cols-lg-auto g-3 align-items-center my-3">
        <div class="col-12">
          <div class="input-group">
            <input type="text" class="form-control" placeholder="File ID" />
          </div>
        </div>
        <div class="col-12">
          <button type="submit" class="btn btn-danger">
            Remove
          </button>
        </div>
      </form>
    </>
  );
}
