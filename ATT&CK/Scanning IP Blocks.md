---
title: Scanning IP Blocks
tags: [Active Scanning]

---

# 基本介紹
攻擊者在「偵察 (reconnaissance) 階段」會做的一件事 —— 掃描 IP 位址區塊。

一個組織可能不只擁有一個 IP，而是一整段（像一條街有好多門牌號碼）。攻擊者要知道:
* 哪些 IP 有在用？（活著的主機）
* 這些 IP 上跑了什麼服務？（例如：網站伺服器、郵件伺服器）
* 服務的版本？（老舊版本可能有漏洞）
這樣攻擊者才能決定下一步從哪裡下手。

# 掃描的方式
**簡單 Ping 掃描**
就像敲門：丟個 ICMP 請求，看看有沒有回應。
**進階掃描**
連到伺服器的服務（例如 HTTP、FTP），看看對方回傳的banner。

:::spoiler
在資安或網路裡講的 banner，其實就是「服務在一開始回應時透露出來的一小段文字資訊」。
:::

**掃描到的資訊可以幫助攻擊者：**
* 進一步偵察 → 例如去查這些主機的網域名稱、技術文件。
* 建立攻擊資源 → 例如知道哪些服務可被利用，準備工具。
* 取得初始存取 → 找到一個有漏洞的服務，就能直接入侵。

:::success
攻擊者就像小偷在小區裡走來走去，先數一數哪些房子有燈亮（活著的 IP），再看看大門是鐵門還是木門（伺服器類型），門鎖新不新（版本）。最後挑一個最好突破的地方下手。banner 就像門口的招牌。
:::

# 練習
**Port scanner**
用 socket 嘗試連線某台主機的常見 port。

**Script**
```python=
import socket

target = "127.0.0.1"
#這裡可以更變目標主機

common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 3389]
#常見的Port

print(f"Scanning {target}...\n")

for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((target ,port))
        if result ==0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSE")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
    finally:
        sock.close()
```
**語法解釋**
```
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
1.這一行是 建立一個「網路連線的工具」，也就是我們要用來掃描 port 的物件。
socket.AF_INET：表示我們要用 IPv4 位址（例如 127.0.0.1）。
如果是 IPv6，就會用 socket.AF_INET6。

socket.SOCK_STREAM：表示這個連線是 TCP 連線（像網頁、SSH、FTP 用的協議）。
如果你要掃描 UDP port，就會用 socket.SOCK_DGRAM。

:::info
簡單來說，這行是在說：我要建立一個「用 IPv4 和 TCP 連線的網路工具」。
:::

```
sock.settimeout(1)
```
這一行是在告訴 Python：如果我連線這個 port 超過 1 秒沒有回應，就不要卡住，直接算「失敗」。

為什麼要加這行？
因為有些 port 根本沒開，如果不設定 timeout，程式會卡很久，掃描速度會超慢。

你也可以改成 0.5 秒，掃描更快，但有些開著的 port 可能沒辦法即時回應，會誤判成關閉。

```
result = sock.connect_ex((target ,port))
```
這行就是做「建立連線」的動作，那要注意socket.connect_ex() 在 Python 3 中只接受一個參數，而且這個參數必須是一個 (host, port) tuple，不能分開兩個參數。

**具體理解**
首先設定好目標主機(target)和要掃描的Port，接著建立一個掃描的物件(要設定IPv4或IPv6，以及TCP或UDP)，最後使用for迴圈，逐個Port去進行掃描，確認是否有使用。

:::spoiler
Port	服務（常見用途）
21	FTP（檔案傳輸）
22	SSH（遠端登入）
23	Telnet（遠端登入，但不安全）
25	SMTP（郵件傳送）
53	DNS（網域名稱解析）
80	HTTP（網站）
110	POP3（郵件接收）
139	NetBIOS（檔案分享、Windows 網路）
143	IMAP（郵件接收）
443	HTTPS（安全網站）
445	SMB（Windows 檔案分享）
3389	RDP（遠端桌面）
:::

# 參考資料
[https://attack.mitre.org/techniques/T1595/](https://)