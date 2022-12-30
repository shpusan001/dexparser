import { useState } from "react";

export default function CodeListItem(props) {
  const [item, setItem] = useState(props.item);
  const [line, setLine] = useState(item.line);
  const [code, setCode] = useState(item.code);

  return (
    <>
      <div class="list-group w-auto mb-2 ">
        <div class=" list-group-item list-group-item-action d-flex gap-3 py-3 d-flex gap-2 w-100 justify-content-between">
          <div class="row">
            <p class="col mb-0 opacity-75 text-break text-primary text-break">
              {line}
            </p>
            <p class="col-sm-12 mb-0 opacity-75 text-break code">{code}</p>
          </div>
        </div>
      </div>
    </>
  );
}
