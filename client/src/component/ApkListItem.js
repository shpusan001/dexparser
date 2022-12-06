export default function ApkListItem(props) {
  return (
    <>
      <div class="mb-2 list-group w-auto">
        <div class=" list-group-item list-group-item-action d-flex gap-3 py-3 d-flex gap-2 w-100 justify-content-between">
          <div>
            <h6 class="mb-1">{props.fileName}</h6>
            <p class="mb-0 opacity-75">
              {" "}
              <b>{"file_id: "}</b>
              {props.fileId}
            </p>
            <p class="mb-0 opacity-75">
              <b>{"sha1: "}</b>
              {props.sha1}
            </p>
          </div>
        </div>
      </div>
    </>
  );
}
