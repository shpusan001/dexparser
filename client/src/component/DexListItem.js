import { useEffect, useState } from "react";
import DexListClassItem from "./DexListClassItem";
import DexListFieldItem from "./DexListFieldItem";
import DexListFileItem from "./DexListFileItem";
import DexListMethodItem from "./DexListMethodItem";

export default function DexListItem(props) {
  const [unit, setUnit] = useState(<></>);

  useEffect(() => {
    const type = props.item.type;
    switch (type) {
      case "file":
        setUnit(<DexListFileItem item={props.item} />);
        break;
      case "class":
        setUnit(<DexListClassItem item={props.item} />);
        break;
      case "method":
        setUnit(<DexListMethodItem item={props.item} />);
        break;
      case "field":
        setUnit(<DexListFieldItem item={props.item} />);
        break;
    }
  }, []);

  return <>{unit}</>;
}
