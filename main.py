from bs4 import BeautifulSoup

# ユーザーから提供されたHTMLテキスト
html_content = """
<p data-index="178" class="group/block px-6 pb-2 leading-[17px] [&amp;&gt;[data-clipped=true]:has(~[data-clipped=true]:hover)]:bg-[#EBFFFB]" data-time="2312864" data-active="false"><span class="cursor-pointer text-[13px] text-base-600 font-semibold block select-none" data-speaker="true" data-read="false" data-time="2312864"><a href="https://tldv.io/app/meetings?t=2312.864" class="hidden text-primary-400">38:32 </a><span class="text-base-800 font-medium">イマムラヒデユキ</span><span class="hidden">: </span></span><span data-clipped="false" class="cursor-pointer font-normal text-[13px] text-base-500 data-[active=true]:!text-primary-400 data-[highlighted=true]:bg-yellow-400 data-[highlighted=true]:text-base-700 data-[clipped=true]:bg-[#EBFFFB] peer" data-speaker="false" data-read="false" data-time="2312864">はい、ありがとうございました。</span><span data-clipped="false" class="cursor-pointer font-normal text-[13px] text-base-500 data-[active=true]:!text-primary-400 data-[highlighted=true]:bg-yellow-400 data-[highlighted=true]:text-base-700 data-[clipped=true]:bg-[#EBFFFB] peer" data-speaker="false" data-read="false" data-time="2314358">いたします。</span></p><p data-index="179" class="group/block px-6 pb-2 leading-[17px] [&amp;&gt;[data-clipped=true]:has(~[data-clipped=true]:hover)]:bg-[#EBFFFB]" data-time="2316504" data-active="false"><span class="cursor-pointer text-[13px] text-base-600 font-semibold block select-none" data-speaker="true" data-read="false" data-time="2316504"><a href="https://tldv.io/app/meetings?t=2316.504" class="hidden text-primary-400">38:36 </a><span class="text-base-800 font-medium">Litable事務局</span><span class="hidden">: </span></span><span data-clipped="false" class="cursor-pointer font-normal text-[13px] text-base-500 data-[active=true]:!text-primary-400 data-[highlighted=true]:bg-yellow-400 data-[highlighted=true]:text-base-700 data-[clipped=true]:bg-[#EBFFFB] peer" data-speaker="false" data-read="false" data-time="2316504">失礼いたします。</span></p><span class="cursor-pointer text-[13px] text-base-600 font-semibold block select-none" data-speaker="true" data-read="false" data-time="2316504"><a href="https://tldv.io/app/meetings?t=2316.504" class="hidden text-primary-400">38:36 </a><span class="text-base-800 font-medium">Litable事務局</span><span class="hidden">: </span></span><span data-clipped="false" class="cursor-pointer font-normal text-[13px] text-base-500 data-[active=true]:!text-primary-400 data-[highlighted=true]:bg-yellow-400 data-[highlighted=true]:text-base-700 data-[clipped=true]:bg-[#EBFFFB] peer" data-speaker="false" data-read="false" data-time="2316504">失礼いたします。</span><p data-index="179" class="group/block px-6 pb-2 leading-[17px] [&amp;&gt;[data-clipped=true]:has(~[data-clipped=true]:hover)]:bg-[#EBFFFB]" data-time="2316504" data-active="false"><span class="cursor-pointer text-[13px] text-base-600 font-semibold block select-none" data-speaker="true" data-read="false" data-time="2316504"><a href="https://tldv.io/app/meetings?t=2316.504" class="hidden text-primary-400">38:36 </a><span class="text-base-800 font-medium">Litable事務局</span><span class="hidden">: </span></span><span data-clipped="false" class="cursor-pointer font-normal text-[13px] text-base-500 data-[active=true]:!text-primary-400 data-[highlighted=true]:bg-yellow-400 data-[highlighted=true]:text-base-700 data-[clipped=true]:bg-[#EBFFFB] peer" data-speaker="false" data-read="false" data-time="2316504">失礼いたします。</span></p>
"""

def parse_transcript(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    
    # data-speaker 属性を持つすべての要素を順番に取得
    # これにより、pタグの外にある要素や入れ子構造に関係なく、上から順に処理できます
    elements = soup.find_all(attrs={"data-speaker": True})
    
    current_speaker = "Unknown"
    
    for el in elements:
        # data-speaker="true" は発言者名のラベル
        if el['data-speaker'] == "true":
            # 名前はさらに内側の text-base-800 クラスに入っている
            name_tag = el.find(class_="text-base-800")
            if name_tag:
                current_speaker = name_tag.get_text(strip=True)
        
        # data-speaker="false" は発言内容
        elif el['data-speaker'] == "false":
            text_content = el.get_text(strip=True)
            
            # 結果リストに追加
            results.append({
                "Speaker": current_speaker,
                "Content": text_content
            })

    return results

# 実行と表示
transcript = parse_transcript(html_content)

# 結果を見やすく表示
print(f"{'Speaker':<20} | {'Content'}")
print("-" * 50)
for item in transcript:
    print(f"{item['Speaker']:<20} | {item['Content']}")