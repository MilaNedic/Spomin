%rebase('base.tpl')
%import model
<h1 style="font-size:50px;"><b>Spomin</b></h1>

<blockquote>
    <h3><i>Spomin je najboljša igra za urjenje spomina ;).</i></h3>
</blockquote>


<table>

    <tr>
        <td><b>Izberi težavnost:</b></td>
    </tr>
    
    <tr>
        <td>
            <form action="/nova_igra/" method="POST">
                <input type="radio" name="tezavnost" value="2"> Lahko<br>
                <input type="radio" name="tezavnost" value="3"> Srednje<br>
                <input type="radio" name="tezavnost" value="3"> Tezko<br>  
                <p><input type="submit" value="prični igro"></p>
            </form>
        </td>
    </tr>

    
</table>
