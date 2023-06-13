dados = [
    {"Nome": "Alice", "Idade": 25},
    {"Nome": "Bob", "Idade": 30},
    {"Nome": "Charlie", "Idade": 28}
]

html = """
<!DOCTYPE html>
<html>
<head>
  <style>
    /* Estilo hacker para a tabela */
    body {
      background-color: #000;
      color: #0f0;
      font-family: monospace;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    table {
      border-collapse: collapse;
      width: 50%;
    }

    th, td {
      border: 1px solid #0f0;
      padding: 8px;
      text-align: left;
    }

    th {
      background-color: #f00;
    }

    button {
            background-color: #0f0;
            color: #000;
            border: none;
            padding: 10px 20px;
            margin: 10px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
  </style>
</head>
<body>
  <h1>Tabela controle da População</h1>
  
 <button><a href="index.html">Inicio</a></button>
 
  <table>
    <tr>
      <th>Nome</th>
      <th>Idade</th>
    </tr>
"""

for item in dados:
    html += "<tr>"
    html += "<td>{}</td>".format(item["Nome"])
    html += "<td>{}</td>".format(item["Idade"])
    html += "</tr>"

html += """
  </table>

 
  
</body>
</html>
"""

with open("population_table.html", "w") as file:
    file.write(html)
