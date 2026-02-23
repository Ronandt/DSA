
class SolutionTroll:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "棟梁跋扈"
        return "四面楚歌".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "棟梁跋扈":
            return []
        return s.split("四面楚歌")
