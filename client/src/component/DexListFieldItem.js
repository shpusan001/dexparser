import { useEffect, useState } from "react";

export default function DexListFieldItem(props) {
  const [item, setItem] = useState(props.item);
  const [name, setName] = useState(item.name);
  const [itype, setItype] = useState(item.itype);
  const [ttype, setTtype] = useState(item.ttype);
  const [access, setAccess] = useState(item.access);

  useEffect(() => {
    if (access != undefined) {
      let tmpAccess = "";
      for (let i = 0; i < access.length; i++) {
        tmpAccess = tmpAccess + access[i] + " ";
      }
      setAccess(tmpAccess);
    }
  }, []);

  return (
    <>
      <div class="list-group w-auto mb-2 ms-4">
        <div class=" list-group-item list-group-item-action d-flex gap-3 py-3 d-flex gap-2 w-100 justify-content-between">
          <div>
            <h6 class="mb-0 text-break">{name}</h6>
            <p class="mb-0 opacity-75 text-break text-primary">{itype}</p>
            <p class="mb-0 opacity-75 text-break">type: {ttype}</p>
            <p class="mb-0 opacity-75 text-break">access: {access}</p>
          </div>
        </div>
      </div>
    </>
  );
}
