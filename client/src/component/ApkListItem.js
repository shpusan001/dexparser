export default function ApkListItem(props) {
  return (
    <>
      <div class="list-group w-auto">
        <div class=" list-group-item list-group-item-action d-flex gap-3 py-3 d-flex gap-2 w-100 justify-content-between">
          <div>
            <h6 class="mb-0">{props.fileName}</h6>
            <p class="mb-0 opacity-75">{props.fileId}</p>
          </div>
        </div>
      </div>
    </>
  );
}
