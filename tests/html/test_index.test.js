/** @jest-environment jsdom */
describe('Data Table', () => {
    beforeEach(() => {
        document.body.innerHTML = '<table id="data-table"><tr><th>Loading...</th></tr></table>';
        global.fetch = jest.fn(() =>
            Promise.resolve({
                text: () => Promise.resolve('1,2,3\n4,5,6')
            })
        );
    });
    test('loads CSV into table', () => {
        return fetch('data.csv')
            .then(response => response.text())
            .then(data => {
                const rows = data.split('\n').map(row => row.split(','));
                const table = document.getElementById('data-table');
                table.innerHTML = '';
                rows.forEach(row => {
                    const tr = document.createElement('tr');
                    row.forEach(cell => {
                        const td = document.createElement('td');
                        td.textContent = cell;
                        tr.appendChild(td);
                    });
                    table.appendChild(tr);
                });
                expect(table.querySelectorAll('tr').length).toBe(2);
            });
    });
});