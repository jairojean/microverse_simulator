class building_interface:
    def building_story_interface(data):
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                 body {
                        background-color: #000;
                        font-family: 'Courier New', monospace;
                        color: #fff;
                        margin: 0;
                        padding: 0;
                    }
                .box {
                    padding: 20px;
                    margin: 20px;
                    background-color: #111;
                    box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
                }
                h1{
                  text-align: center;
                }
                
                .box-header {
                    background-color:  #5CB85C;
                    color: #000;
                    padding: 10px;
                    font-weight: bold;
                    text-align: center;
                }
                .box-content {
                    margin-top: 20px;
                    color: #fff;
                }
                .button-container {
                    margin-top: 30px;
                    display: flex;
                    justify-content: center;
                }
                .button {
                        background-color: #5CB85C; /* Verde */
                        color: #000;
                        border: none;
                        padding: 10px 20px;
                        margin: 10px;
                        font-size: 16px;
                        border-radius: 5px;
                        cursor: pointer;
                        transition: background-color 0.3s ease;
                    }
                table {
                    width: 80%;
                    max-height: 400px;
                    overflow-y: scroll;
                    margin-top: 30px;
                    border-collapse: collapse;
                }
                th, td {
                    border: 1px solid #0f0;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #0f0;
                    color: #000;
                    position: sticky;
                    top: 0;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h1> História da População</h1>
            <div class="button-container">
                <a href="index.html"><button class="button">Início</button></a>
                <a href="population_table.html"><button class="button">Tabela População</button></a>
                <a href="population_story.html"><button class="button">História da População</button></a>
            </div>
        """
        for item in data:
            html += """
            <div class="box">
                <div class="box-header"> 
                    <span style="font-size: 20px;">CPF:</span> {} <span style="font-size: 20px;">Nome:</span> {}
                </div>
                <div class="box-content">
                    <span style="font-size: 18px;">De CPF {} nascido em {},</span>
                    <span style="font-size: 18px;">{} do sexo {}, com a característica de {}</span>
                    <span style="font-size: 18px;">possui um relacionamento com {} de CPF {} sendo então uma pessoa {}</span>
                </div>
            """.format(item.id, item.name, item.id, item.birth_date, item.name, item.gender, item.personality,
                       item.partner, item.id_partner, item.marital_status)

            if item.status_life == 'Morte':
                html += """
                <div class="box-content"><span style="font-size: 18px;">{} morreu no ano de {} aos {} anos de idade de {}</span></div>
                """.format(item.name, item.death_date, item.age_death, item.cause_death)
            else:
                html += """
                <div class="box-content"><span style="font-size: 18px;">Hoje {} está com {} anos de idade</span></div>
                """.format(item.name, item.age)
            html += "</div>"
        html += """
        </body>
        </html>
        """
        with open("view/population_story.html", "w") as file:
            file.write(html)

    def build_table_interface(data):
        html = """
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {
                        background-color: #000;
                        font-family: 'Courier New', monospace;
                        color: #fff;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        height: 100vh;
                    }
                    .button-container {
                        margin-top: 30px;
                    }
                    .button {
                        background-color: #5CB85C;
                        color: #000;
                        border: none;
                        padding: 10px 20px;
                        margin: 10px;
                        font-size: 16px;
                        border-radius: 5px;
                        cursor: pointer;
                        transition: background-color 0.3s ease;
                    }

                    table {
                        width: 80%;
                        max-height: 400px;
                        overflow-y: scroll;
                        margin-top: 30px;
                    }

                    th, td {
                        border: 1px solid #5CB85C;
                        padding: 8px;
                        text-align: left;
                    }

                    th {
                        background-color: #5CB85C;
                        color: #FFF;
                        position: sticky;
                        top: 0;
                        font-weight: bold;
                    }
                </style>
            </head>
            <body>
              <h1> Tabela da População</h1>
              <div class="button-container">
                  <a href="index.html"><button class="button">Início</button></a>
                  <a href="population_table.html"><button class="button">Tabela População</button></a>
                  <a href="population_story.html"><button class="button">História da População</button></a>
              </div>
              <table>
                <tr>
                  <th>CPF</th>
                  <th>Data Nascimento</th>
                  <th>Idade</th>
                  <th>Nome</th>
                  <th>Estado Civil</th>
                  <th>Parceiro</th>
                  <th>CPF do Parceiro</th>
                </tr>
        """
        for item in data:
            html += "<tr>"
            html += "<td>{}</td>".format(item.id)
            html += "<td>{}</td>".format(item.birth_date)
            html += "<td>{}</td>".format(item.age)
            html += "<td>{}</td>".format(item.name)
            html += "<td>{}</td>".format(item.marital_status)
            html += "<td>{}</td>".format(item.partner)
            html += "<td>{}</td>".format(item.id_partner)
            html += "</tr>"
        html += """
              </table>
            </body>
            </html>
        """
        with open("view/population_table.html", "w") as file:
            file.write(html)