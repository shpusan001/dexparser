import { useState } from "react";

export default function DexListFileItem(props) {
  const [item, setItem] = useState(props.item);
  const [name, setName] = useState(item.name);

  return (
    <>
      <div class="list-group w-auto mb-2">
        <div class=" list-group-item list-group-item-action d-flex gap-3 py-3 d-flex gap-2 w-100 justify-content-between bg-opacity-75">
          <div>
            <h6 class="mb-0 text-break">{name}</h6>
          </div>
        </div>
      </div>
    </>
  );
}
