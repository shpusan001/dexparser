import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { getConvHex2Smali, setSelectedMethod } from "../module/dex";

export default function DexListMethodItem(props) {
  const dispatch = useDispatch();

  const [item, setItem] = useState(props.item);
  const [clazz, setClazz] = useState(item.class);
  const [name, setName] = useState(item.name);
  const [itype, setItype] = useState(item.itype);
  const [rtype, setRtype] = useState(item.rtype);
  const [access, setAccess] = useState(item.access);
  const [parameters, setParameters] = useState(item.parameters);
  const [code, setCode] = useState(item.code);

  useEffect(() => {
    if (access != undefined) {
      let tmpAccess = "";
      for (let i = 0; i < access.length; i++) {
        tmpAccess = tmpAccess + access[i] + " ";
      }
      setAccess(tmpAccess);
    }

    if (parameters != undefined) {
      let tmpParameters = "";
      for (let i = 0; i < parameters.length; i++) {
        tmpParameters = tmpParameters + parameters[i] + " ";
      }
      setParameters(tmpParameters);
    }
  }, []);

  const onClick = (e) => {
    const data = {
      class: clazz,
      method: name,
    };
    dispatch(setSelectedMethod(data));
    dispatch(getConvHex2Smali({ hexcode: code }));
  };

  return (
    <>
      <div class="list-group w-auto mb-2 ms-4" onClick={onClick}>
        <div class=" list-group-item list-group-item-action d-flex gap-3 py-3 d-flex gap-2 w-100 justify-content-between">
          <div>
            <h6 class="mb-0 text-break">{name}</h6>
            <p class="mb-0 opacity-75 text-break text-primary">{itype}</p>
            <p class="mb-0 opacity-75 text-break">return: {rtype}</p>
            <p class="mb-0 opacity-75 text-break">access: {access}</p>
            <p class="mb-0 opacity-75 text-break">parameters: {parameters}</p>
          </div>
        </div>
      </div>
    </>
  );
}
