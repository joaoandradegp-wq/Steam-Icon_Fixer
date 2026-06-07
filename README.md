<h1 align="center">🎮 Steam Icon Fixer</h1>

<p align="center">
Ferramenta simples e automatizada para corrigir ícones quebrados, ausentes ou em branco de jogos da Steam no Desktop.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Ativo-success">
  <img src="https://img.shields.io/badge/Linguagem-Python-blue">
  <img src="https://img.shields.io/badge/Tipo-Utility-lightgrey">
</p>

---

## 📌 Sobre

O **Steam Icon Fixer** foi desenvolvido para resolver um problema comum no Windows:  
ícones de jogos da Steam que desaparecem, ficam genéricos, quebrados ou totalmente em branco no Desktop.

O aplicativo escaneia automaticamente os atalhos `.url`, identifica os jogos da Steam e baixa novamente os ícones originais diretamente da CDN oficial da Steam.

Todo o processo é automatizado, incluindo atualização dos atalhos e notificação imediata do Windows para recarregar os ícones sem necessidade de reiniciar o Explorer.

---

## ⚙️ Funcionalidades

<table style="border: none; border-collapse: collapse;">

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🔍 ESCANEAMENTO AUTOMÁTICO

Localiza automaticamente atalhos da Steam no Desktop (incluindo OneDrive), identificando arquivos `.url` com `steam://rungameid`.

<br><br>
</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🎯 IDENTIFICAÇÃO DE JOGOS

Extrai o GameID diretamente do atalho e utiliza esse identificador para buscar o ícone correto na Steam.

<br>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### ⬇️ DOWNLOAD AUTOMÁTICO DE ÍCONES

Baixa os ícones diretamente da CDN oficial da Steam garantindo arquivos válidos e atualizados.

Inclui validação de tamanho para evitar ícones corrompidos.

<br><br>
</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🔄 ATUALIZAÇÃO DE ATALHOS

Atualiza automaticamente o caminho do ícone dentro do arquivo `.url`, garantindo que o Windows utilize o novo arquivo.

<br>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🆕 SISTEMA PROGRESSIVO DE ÍCONES

A cada correção o programa gera uma nova versão do ícone:

`_new1`, `_new2`, `_new3`, `_new4`...

Isso força o Windows a utilizar um novo arquivo e reduz drasticamente problemas causados por cache persistente.

<br><br>
</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### ⚡ ATUALIZAÇÃO IMEDIATA DO WINDOWS

Após corrigir o atalho, o programa notifica automaticamente o Windows Shell para atualizar os ícones sem necessidade de reiniciar o Explorer.

<br>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🧠 TRATAMENTO INTELIGENTE DE ARQUIVOS

Remove versões antigas relacionadas ao mesmo ícone, evita duplicações e mantém consistência entre os atalhos e arquivos baixados.

<br><br>
</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 📊 INTERFACE COM LOG E PROGRESSO

Interface simples com barra de progresso e log em tempo real mostrando cada etapa do processo.

<br>
</td>
</tr>

</table>

---

## 🚀 Como usar

1. Clique em **Escanear Desktop**
2. Clique em **Corrigir Tudo**
3. Aguarde o processamento automático
4. Os atalhos serão atualizados automaticamente

Não é mais necessário limpar cache manualmente nem reiniciar o Explorer.

---

## 🎯 Problema resolvido

- Ícones genéricos da Steam
- Ícones quebrados ou ausentes
- Ícones totalmente brancos
- Cache persistente do Windows
- Atalhos com caminhos inválidos
- Reutilização incorreta de ícones antigos pelo Windows

---

## 📸 Preview

<p align="center">
  <img width="500" alt="image" src="https://github.com/user-attachments/assets/4f209275-ce40-401c-924f-ad2906ee4ccd" />
</p>

---

## 📥 Download

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/Download-Steam%20Icon%20Fixer-blue?style=for-the-badge">
  </a>
</p>

---

<p align="center">
Feito para automatizar o que ninguém deveria corrigir manualmente. 😄
</p>
