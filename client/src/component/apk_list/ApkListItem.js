import { CopyToClipboard } from "react-copy-to-clipboard";

export default function ApkListItem(props) {
  return (
    <>
      <CopyToClipboard text={props.fileId}>
        <div class="mb-2 list-group w-auto ">
          <div class=" list-group-item list-group-item-action d-flex gap-3 py-3 d-flex gap-2 w-100 justify-content-between ">
            <div class="text-break">
              <h6 class="mb-1 ">{props.fileName}</h6>
              <p class="mb-0 opacity-75 ">
                <b>{"file_id: "}</b>
                <text>{props.fileId}</text>
              </p>
              <p class="mb-0 opacity-75">
                <b>{"sha1: "}</b>
                {props.sha1}
              </p>
            </div>
          </div>
        </div>
      </CopyToClipboard>
    </>
  );
}
