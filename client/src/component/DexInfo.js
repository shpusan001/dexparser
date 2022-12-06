import CodeBox from "../component/CodeBox";
import DexListItem from "../component/DexListItem";

export default function DexInfo() {
  return (
    <>
      <div class="row">
        <div class="col me-2 bg-primary">
          <DexListItem info={{ type: "type", name: "name" }} />
        </div>
        <div class="col m2-2">
          <CodeBox />
        </div>
      </div>
    </>
  );
}
